import TimelineView from './TimelineView';

export default function DataViewer({ items, hint }) {
  if (!items || items.length === 0) return null;

  if (hint === 'timeline') {
    return <TimelineView items={items} />;
  }

  if (hint === 'text') {
    return (
      <div className="bg-white p-4 rounded shadow">
        <p className="text-gray-700">{items[0]?.text || 'No content.'}</p>
      </div>
    );
  }

  return (
    <div className="bg-yellow-100 p-4 rounded border-l-4 border-yellow-400 text-yellow-900">
      Unknown display hint: {hint}
    </div>
  );
}
