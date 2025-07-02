export default function QueryInput({ query, setQuery, onSubmit }) {
  return (
    <div className="flex items-center gap-2 mb-4">
      <input
        type="text"
        className="flex-1 p-2 border rounded"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="e.g. What jobs has Connor had?"
        onKeyDown={(e) => e.key === 'Enter' && onSubmit()}
      />
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        onClick={onSubmit}
      >
        Ask
      </button>
    </div>
  );
}
