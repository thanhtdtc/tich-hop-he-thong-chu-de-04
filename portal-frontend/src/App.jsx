import { useState } from "react";
import { Input, Alert, Card, Descriptions, Table, Tag } from "antd";

const ID_REGEX = /^B\d{2}DC[A-Z]{2}\d{3}$/;
const API = import.meta.env.VITE_PORTAL_API ?? "http://localhost:8080";

export default function App() {
  const [data, setData] = useState(null);
  const [notice, setNotice] = useState(null);
  const [loading, setLoading] = useState(false);

  async function search(value) {
    const id = value.trim();
    if (!ID_REGEX.test(id)) {
      setData(null);
      setNotice({ type: "error", text: "Mã sinh viên sai định dạng" });
      return;
    }
    setLoading(true);
    try {
      const res = await fetch(`${API}/api/portal/students/${id}/summary`);
      const body = await res.json();
      if (!res.ok) {
        setData(null);
        setNotice({ type: "error", text: body.message });
      } else {
        setData(body);
        setNotice(
          body.warnings.length
            ? { type: "warning", text: body.warnings.join(". ") }
            : null
        );
      }
    } catch {
      setData(null);
      setNotice({ type: "error", text: "Không kết nối được Portal backend" });
    } finally {
      setLoading(false);
    }
  }

  const columns = [
    { title: "Học kỳ", dataIndex: "semester" },
    { title: "Số tiền (VNĐ)", dataIndex: "amount", render: (v) => v.toLocaleString("vi-VN") },
    { title: "Hạn đóng", dataIndex: "dueDate" },
    {
      title: "Trạng thái",
      dataIndex: "status",
      render: (s) => <Tag color={s === "PAID" ? "green" : "red"}>{s}</Tag>,
    },
  ];

  const owed = (data?.tuitions ?? [])
    .filter((t) => t.status === "UNPAID")
    .reduce((sum, t) => sum + t.amount, 0);

  return (
    <div style={{ maxWidth: 800, margin: "40px auto", padding: 16 }}>
      <h2>Tra cứu sinh viên</h2>
      <Input.Search
        placeholder="Nhập mã sinh viên, ví dụ B22DCCN001"
        enterButton="Tra cứu"
        loading={loading}
        onSearch={search}
      />
      {notice && (
        <Alert style={{ marginTop: 16 }} type={notice.type} message={notice.text} showIcon />
      )}
      {data && (
        <>
          <Card title="Thông tin sinh viên" style={{ marginTop: 16 }}>
            <Descriptions column={1}>
              <Descriptions.Item label="Họ tên">{data.student.fullName}</Descriptions.Item>
              <Descriptions.Item label="Email">{data.student.email}</Descriptions.Item>
              <Descriptions.Item label="Lớp">{data.student.className}</Descriptions.Item>
              <Descriptions.Item label="Ngành">{data.student.major}</Descriptions.Item>
            </Descriptions>
          </Card>
          {data.tuitions && (
            <Card
              title={`Học phí (còn nợ: ${owed.toLocaleString("vi-VN")} VNĐ)`}
              style={{ marginTop: 16 }}
            >
              <Table rowKey="id" columns={columns} dataSource={data.tuitions} pagination={false} />
            </Card>
          )}
        </>
      )}
    </div>
  );
}