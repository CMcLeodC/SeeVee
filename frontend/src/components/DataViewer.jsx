export default function DataViewer({ items, hint }) {
  return (
    <div className="space-y-4">
      {items.map((item) => (
        <div key={item.id} className="bg-white p-4 rounded shadow">
          <h3 className="text-lg font-semibold">{item.title} @ {item.company}</h3>
          <p className="text-sm text-gray-600 mb-2">
            {item.start_date} — {item.end_date || 'Present'}
          </p>
          <p>{item.description}</p>
        </div>
      ))}
    </div>
  );
}
