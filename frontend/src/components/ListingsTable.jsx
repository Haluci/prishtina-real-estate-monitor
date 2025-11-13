
import { useEffect, useState } from 'react';

export default function ListingsTable() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/listings')
      .then(r => r.json())
      .then(d => setData(d));
  }, []);

  return (
    <table className="w-full bg-white shadow-md rounded mt-4">
      <thead>
        <tr className="bg-gray-200">
          <th className="p-2">Price</th>
          <th className="p-2">m²</th>
          <th className="p-2">Location</th>
          <th className="p-2">Floor</th>
          <th className="p-2">Scam Score</th>
        </tr>
      </thead>
      <tbody>
        {data.map((x,i) => (
          <tr key={i} className="border-b">
            <td className="p-2">{x[2]}</td>
            <td className="p-2">{x[3]}</td>
            <td className="p-2">{x[4]}</td>
            <td className="p-2">{x[5]}</td>
            <td className="p-2">{x[10]}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
