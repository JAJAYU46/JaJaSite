/** Accept only YouTube video/playlist URLs; never interpolate arbitrary embed URLs. */
export function youtubeEmbed(value?: string): string | null {
  if (!value) return null;
  try {
    const url = new URL(value);
    if (url.protocol !== 'https:') return null;
    const host = url.hostname.replace(/^www\./, '');
    if (!['youtu.be', 'youtube.com', 'm.youtube.com'].includes(host)) return null;
    const video = host === 'youtu.be' ? url.pathname.slice(1) : url.searchParams.get('v') || (url.pathname.startsWith('/embed/') ? url.pathname.split('/')[2] : null);
    const playlist = url.searchParams.get('list');
    if (video && /^[\w-]{11}$/.test(video)) return `https://www.youtube-nocookie.com/embed/${video}`;
    if (playlist && /^[\w-]+$/.test(playlist)) return `https://www.youtube-nocookie.com/embed/videoseries?list=${playlist}`;
  } catch { /* Invalid URLs leave the normal image hero available. */ }
  return null;
}
