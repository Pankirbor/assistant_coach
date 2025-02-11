import React, { useEffect, useState } from "react";
import axios from "axios";

// Типы для данных клиента
interface Client {
  id: number;
  telegram_id: number;
  username: string;
  first_name: string;
  last_name: string;
  email: string;
}

const ClientInfo: React.FC = () => {
  const [client, setClient] = useState<Client | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Загрузка данных о клиенте
  useEffect(() => {
    const fetchClient = async () => {
      try {
        const response = await axios.get<Client>("/api/users/1/");
        setClient(response.data);
      } catch (err) {
        setError("Ошибка при загрузке данных о клиенте");
      } finally {
        setLoading(false);
      }
    };

    fetchClient();
  }, []);

  if (loading) {
    return <div>Загрузка...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  if (!client) {
    return <div>Данные о клиенте не найдены</div>;
  }

  return (
    <div>
      <h2>Информация о клиенте</h2>
      <div>
        <p>ID:</p>
        <p>{client.id}</p>

        <p>Telegram ID:</p>
        <p>{client.telegram_id}</p>

        <p>Имя пользователя:</p>
        <p>{client.username}</p>

        <p>Имя:</p>
        <p>{client.first_name || "Не указано"}</p>

        <p>Фамилия:</p>
        <p>{client.last_name || "Не указано"}</p>

        <p>Email:</p>
        <p>{client.email}</p>
      </div>
    </div>
  );
};

// Стили для компонента
const styles = {
  container: {
    maxWidth: "600px",
    margin: "0 auto",
    padding: "20px",
    border: "1px solid #ddd",
    borderRadius: "8px",
    backgroundColor: "#f9f9f9",
    boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
  },
  header: {
    textAlign: "center",
    color: "#333",
    marginBottom: "20px",
  },
  infoContainer: {
    display: "grid",
    gridTemplateColumns: "1fr 2fr",
    gap: "10px",
  },
  label: {
    fontWeight: "bold",
    color: "#555",
    margin: "0",
  },
  value: {
    margin: "0",
    color: "#333",
  },
};

export default ClientInfo;