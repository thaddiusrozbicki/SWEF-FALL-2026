# Homework 2 submission

## What I learned

This week I learned how a frontend is put together. I built pages as React components, styled them with Tailwind classes, and added a second page just by making a new folder in `app/`.

## Next.js vs raw HTML/CSS

With raw HTML and CSS I'd need a separate file for every page and I'd have to copy the navbar into each one. In Next.js the navbar lives in `layout.tsx` once and every page gets it. Tailwind also lets me style things right in the markup instead of switching back and forth with a CSS file.

## How the tools fit together

React is the base, where every page is a function that returns JSX. TypeScript adds types on top so mistakes show up before the page runs. Tailwind handles styling through `className`. Next.js ties it together with the project setup, routing, and the shared layout.

## My interest page

My interest page is `/cars`. I've gone to Monterey Car Week the past couple of years, I follow the collector market every day, and I'm the treasurer of the Northeastern Automotive Club. It was an easy pick because it's what I'd be talking about anyway.

## Screenshots

- Home: ![Home page](home.png)
- Interest: ![Cars page](interest.png)

## Project location

`02-frontend/hw/mywebsite`
