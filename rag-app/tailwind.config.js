/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,jsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,jsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,jsx,mdx}",
  ],
  theme: {
    extend: {
      // We've enabled the default slate colors by not overriding them
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
    },
  },
  safelist: [
    'text-sm', 'leading-normal', 'my-2', 'text-xl', 'font-bold', 'my-3',
    'text-lg', 'text-base', 'list-disc', 'pl-5', 'list-decimal',
    'text-blue-600', 'hover:underline', 'pl-4', 'border-l-4', 'border-gray-300', 'italic',
    'rounded-md', 'p-3', 'bg-slate-800', 'text-white', 'overflow-x-auto',
    'font-mono', 'bg-slate-200', 'text-slate-800', 'px-1', 'py-0.5', 'rounded',
    'border-collapse', 'w-full', 'border', 'p-2'
  ],
  plugins: [require("tailwindcss-animate")],
}