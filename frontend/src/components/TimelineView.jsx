import TimelineItem from './TimelineItem';

export default function TimelineView({ items }) {
  return (
    <div className="space-y-6">
      {items.map((item) => (
        <TimelineItem key={item.id} item={item} />
      ))}
    </div>
  );
}
