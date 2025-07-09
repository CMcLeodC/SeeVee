import TimelineItem from './TimelineItem';

export default function TimelineView({ items }) {
  return (
    <div className="relative bg-gray-50 p-4 rounded-lg">
      {items.map((item) => (
        <TimelineItem key={item.id} item={item} />
      ))}
    </div>
  );
}
