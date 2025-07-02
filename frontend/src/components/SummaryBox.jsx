export default function SummaryBox({ text }) {
  return (
    <div className="bg-white p-4 shadow rounded mb-4">
      <p className="text-gray-800">{text}</p>
    </div>
  );
}
