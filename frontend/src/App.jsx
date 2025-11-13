
import ListingsTable from './components/ListingsTable';
import Filters from './components/Filters';

export default function App() {
  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-4">Prishtina Real Estate Dashboard</h1>
      <Filters />
      <ListingsTable />
    </div>
  );
}
