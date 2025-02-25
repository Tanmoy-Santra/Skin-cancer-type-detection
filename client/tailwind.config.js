// /** @type {import('tailwindcss').Config} */
// export default {
//   content: [
//     "./index.html",
//     "./src/**/*.{js,ts,jsx,tsx}",
//   ],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// }


/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      keyframes: {
        moveUpDown: {
          '0%': { transform: 'translateY(0)' },
          '20%': { transform: 'translateY(-10px)' },
          '50%': { transform: 'translateY(10px)' },
          '80%': { transform: 'translateY(-10px)' },
          '100%': { transform: 'translateY(0)' },
        },
      },
      animation: {
        'up-down': 'moveUpDown 2s ease-in-out infinite',
      },
    },
  },
  plugins: [],
}
