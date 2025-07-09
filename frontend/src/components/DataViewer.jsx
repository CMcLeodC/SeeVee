import { BriefcaseIcon, GraduationCapIcon, AlertTriangleIcon, UserIcon } from 'lucide-react';
import { format } from 'date-fns';

export default function DataViewer({ items, hint }) {
  if (!items || items.length === 0) return null;
  const isJob = items[0]?.company_name;
  const isEducation = items[0]?.institution;

  const formatDate = (dateStr) => {
    if (!dateStr) return 'Present';
    return format(new Date(dateStr), 'MMM yyyy');
  };

  // ✅ Detect "profile" info
  if (hint === "profile" || (hint === "text" && items[0]?.email)) {
    const user = items[0];

    return (
      <div className="bg-white p-6 rounded-lg shadow-md max-w-xl mx-auto">
        <h2 className="text-2xl font-bold text-gray-900 mb-2">{user.name}</h2>
        <p className="text-gray-600 mb-2">{user.location}</p>
        <div className="text-sm text-gray-700 space-y-1 mb-4">
          <p>
            <strong>Email:</strong>{" "}
            <a href={`mailto:${user.email}`} className="text-blue-600 hover:underline">
              {user.email}
            </a>
          </p>
          <p><strong>Phone:</strong> {user.phone}</p>
          <p>
            <strong>LinkedIn:</strong>{" "}
            <a href={user.linkedin_url} target="_blank" className="text-blue-600 hover:underline" rel="noopener noreferrer">
              View Profile
            </a>
          </p>
          <p>
            <strong>GitHub:</strong>{" "}
            <a href={user.github_url} target="_blank" className="text-blue-600 hover:underline" rel="noopener noreferrer">
              View Projects
            </a>
          </p>
        </div>
        <p className="text-gray-800 italic">{user.summary}</p>
      </div>
    );
  }


if (hint === "timeline") {
  return (
    <div className="relative border-l-4 border-indigo-300 pl-6 space-y-8">
      {items.map((item) => (
        <div key={item.id} className="relative">
          <div className="absolute -left-3 top-1.5 bg-indigo-500 text-white p-1 rounded-full">
            {isJob ? <BriefcaseIcon size={16} /> : <GraduationCapIcon size={16} />}
          </div>

          <div className="bg-white p-4 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-800">
              {isJob ? item.role : item.qualification}
            </h3>
            <p className="text-sm text-gray-500 mb-1">
              {isJob ? item.company_name : item.institution}
            </p>
            <p className="text-xs text-gray-400 mb-2">
              {formatDate(item.start_date)} – {formatDate(item.end_date)}
            </p>
            <p className="text-gray-700 mb-2">{item.description || item.field_of_study}</p>

            {isJob && item.technologies?.length > 0 && (
              <div className="flex flex-wrap gap-2 mt-2">
                {item.technologies.map((tech, index) => (
                  <span
                    key={index}
                    className="bg-indigo-100 text-indigo-800 text-xs px-2 py-1 rounded-full"
                  >
                    {tech}
                  </span>
                ))}
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  );
  
}

// ✅ Default fallback for generic "text" (e.g. error, no intent match)
  return (
    <div className="bg-white p-4 rounded shadow text-gray-700">
      {items.map((item, idx) => (
        <p key={idx}>{typeof item === 'string' ? item : JSON.stringify(item)}</p>
      ))}
    </div>
  );
}
