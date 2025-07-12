import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        rust: "#B5400C",
        charcoal: "#373A49",
        seasalt: "#F8F8F8",
        taupegray: "#81838B",
        darkorange: "#FF901F",
      },
    },
  },
  plugins: [],
};
export default config;
