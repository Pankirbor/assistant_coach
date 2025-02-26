import React, { useEffect, useState } from "react";
import axios from "axios";
import "./ClientInfo.css"

//* Типы для данных клиента
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
    <div className="container">
      <h2 className="header" >Информация о клиенте</h2>
      <div className="infoContainer">
        <p className="label" >ID:</p>
        <p className="value" >{client.id}</p>

        <p className="label" >Telegram ID:</p>
        <p className="value" >{client.telegram_id}</p>

        <p className="label" >Имя пользователя:</p>
        <p className="value" >{client.username}</p>

        <p className="label" >Имя:</p>
        <p className="value" >{client.first_name || "Не указано"}</p>

        <p className="label" >Фамилия:</p>
        <p className="value" >{client.last_name || "Не указано"}</p>

        <p className="label" >Email:</p>
        <p className="value" >{client.email}</p>
      </div>
    </div>
  );
};




export default ClientInfo;