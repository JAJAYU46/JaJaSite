// Confirm timeline dates before publication. Empty links render disabled controls.
export const portfolio = {
  name: 'Chia-Jung Yu',
  github: 'https://github.com/JAJAYU46',
  linkedin: '',
  resume: '', // Local path under public/, e.g. assets/resume/<your actual filename>.pdf
  email: '',
  homeProjectCount: 6,
};
export const categories = [
  { id: 'robotics', title: 'Robotics & Autonomous Systems', description: 'Perception, planning, and the software that connects them.' },
  { id: 'software', title: 'Software, AI & Data', description: 'Software systems, applied intelligence, and data.' },
  { id: 'embedded', title: 'Embedded & Hardware Engineering', description: 'Where code meets circuits and physical systems.' },
];
export const timeline = [
  { date: '2021–2027', title: 'National Taiwan University', detail: 'Bio-Mechatronics Engineering', icon: '01' },
  { date: '2023–2025', title: 'Robotics Research', detail: 'Robots and Medical Mechatronics Lab', icon: '02' },
  { date: '2025–2026', title: 'International Exchange', detail: 'Warsaw University of Technology · Wageningen University', icon: '03' },
  { date: '2026', title: 'Robotics Software', detail: 'FAST-LIVO2, loop closure & global relocalization', icon: '04' },
  { date: 'Spring 2027', title: 'Boston University', detail: 'Incoming M.S. in Robotics', icon: '05' },
];
export function sortProjects(a: {data: {order: number}}, b: {data: {order: number}}) {
  return a.data.order - b.data.order;
}
