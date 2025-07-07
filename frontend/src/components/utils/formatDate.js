export function formatDate(dateStr) {
  if (!dateStr) return 'Present';
  const date = new Date(dateStr);
  return date.toLocaleDateString('en-GB', {
    month: 'short',
    year: 'numeric',
  });
}
