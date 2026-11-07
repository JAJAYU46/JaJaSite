import { portfolio } from './data/portfolio';

export const SITE_CONFIG = {
  title: "JaJa | Robotics Engineering Portfolio",
  description: "Robotics Software | SLAM | Perception | Autonomous Systems",

  cover: 'assets/images/portfolio-cover.svg',
  logo: 'assets/images/jaja-mark.svg',
  logoDark: 'assets/images/jaja-mark.svg',
  favicon: 'assets/images/jaja-mark.svg',

  navigation: true,
  subscribers: false,

  twitter: '',
  facebook: '',
  xUsername: '',
  github: new URL(portfolio.github).pathname.replace(/^\//, ''),

  disqus: false,
  disqusShortname: '',

  googleAnalytics: '',

  wordsPerMinute: 200,
  pageSize: 25,

  algolia: {
    applicationId: '',
    indexName: '',
    searchOnlyApiKey: '',
  },
};

/**
 * Helper to resolve paths with the Astro base URL
 */
export function getAssetUrl(path: string | null | undefined): string {
  if (!path) return '';
  if (path.startsWith('http://') || path.startsWith('https://') || path.startsWith('//')) {
    return path;
  }
  const base = import.meta.env.BASE_URL; // e.g. "/casper/" or "/"
  const cleanPath = path.replace(/^\//, '');
  return `${base.replace(/\/$/, '')}/${cleanPath}`;
}

/**
 * Strips HTML and markdown formatting to create a text excerpt.
 */
export function getExcerpt(content: string, limit = 33): string {
  const stripped = content
    .replace(/<[^>]*>/g, '') // strip HTML tags
    .replace(/!\[([^\]]*)\]\([^)]+\)/g, '$1') // keep image alt text
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // keep link text
    .replace(/^#{1,6}\s+/gm, '') // strip heading markers
    .replace(/[*`_>~]/g, '') // strip simple markdown symbols
    .replace(/^\s*[-+]\s+/gm, '') // strip unordered list markers
    .replace(/\s+/g, ' ') // normalize whitespace
    .trim();
  const words = stripped.split(' ');
  if (words.length <= limit) return stripped;
  return words.slice(0, limit).join(' ') + '...';
}

/**
 * Calculates reading time based on word count.
 */
export function getReadingTime(content: string, wpm = SITE_CONFIG.wordsPerMinute): string {
  const stripped = content.replace(/<[^>]*>/g, '').trim();
  if (!stripped) return '1 min read';
  const words = stripped.split(/\s+/).length;
  if (words <= wpm) {
    return '1 min read';
  }
  return `${Math.ceil(words / wpm)} min read`;
}
