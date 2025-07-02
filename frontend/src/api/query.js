export async function submitQuery(queryText) {
  const res = await fetch("/query", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query: queryText }),
  });

  if (!res.ok) throw new Error("Query failed");

  return res.json();
}
