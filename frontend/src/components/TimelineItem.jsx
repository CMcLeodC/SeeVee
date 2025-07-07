import { CalendarDaysIcon, BuildingOffice2Icon, AcademicCapIcon } from '@heroicons/react/24/outline';
import { formatDate } from "./utils/formatDate";

export default function TimelineItem({ item }) {
  const isEducation = !!item.institution;

  const title = isEducation
    ? item.qualification
    : item.role;

//   const subtitle = isEducation
//     ? item.institution
//     : item.company_name;

  const description = isEducation
    ? item.field_of_study
    : item.description;

  const technologies = isEducation ? [] : item.technologies || [];

  return (
    <div className="bg-white p-6 rounded-lg shadow-md border">
      <div className="flex items-center justify-between mb-2">
        <div className="flex items-center gap-2">
          {isEducation ? (
            <AcademicCapIcon className="h-6 w-6 text-blue-500" />
          ) : (
            <BuildingOffice2Icon className="h-6 w-6 text-blue-500" />
          )}
          <h3 className="text-lg font-semibold">{title}</h3>
        </div>
        <div className="flex items-center gap-1 text-sm text-gray-500">
          <CalendarDaysIcon className="h-4 w-4" />
          <span>{formatDate(item.start_date)} — {formatDate(item.end_date)}</span>
        </div>
      </div>
      <p className="text-gray-800 leading-relaxed whitespace-pre-line mb-3">{description}</p>
      {technologies.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {technologies.map((tech) => (
            <span key={tech} className="bg-blue-100 text-blue-800 text-xs font-medium px-2 py-1 rounded-full">
              {tech}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}
