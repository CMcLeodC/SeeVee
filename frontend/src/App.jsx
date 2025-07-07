import { useState } from 'react';
import DataViewer from './components/DataViewer'; // ✅ this is what was missing

function App() {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [summary, setSummary] = useState('');
  const [data, setData] = useState([]);
  const [hint, setHint] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setError('');
    setSummary('');
    setData([]);

    try {
      const res = await fetch('http://localhost:8000/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      });

      if (!res.ok) throw new Error('Query failed');

      const result = await res.json();
      setSummary(result.response);
      setData(result.data);
      setHint(result.display_hint); // ✅ important
    } catch (err) {
      console.error(err);
      setError('Something went wrong.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-2xl font-bold mb-4">Ask me anything about Connor’s CV</h1>
        <div className="flex gap-2 mb-4">
          <input
            type="text"
            className="flex-1 p-2 border rounded"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSubmit()}
            placeholder="e.g. What jobs has Connor had?"
          />
          <button
            onClick={handleSubmit}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Ask
          </button>
        </div>

        {loading && <p className="text-gray-600">Loading...</p>}
        {error && <p className="text-red-500">{error}</p>}

        {summary && (
          <div className="bg-white p-4 rounded shadow mb-4">
            <p>{summary}</p>
          </div>
        )}

        {data.length > 0 && <DataViewer items={data} hint={hint} />}
      </div>
    </div>
  );
}

export default App;
