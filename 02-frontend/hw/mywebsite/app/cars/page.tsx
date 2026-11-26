export default function CarsPage() {
  return (
    <main className="w-full max-w-2xl mx-auto px-6 py-16">
      <h1 className="text-5xl font-bold text-red-500 mb-6">Cars</h1>
      <p className="text-lg text-zinc-300 mb-8">
        Cars are the thing I could talk about all day. I’ve gone to Monterey
        Car Week the past couple of years, I check the collector car market
        every day, and I’m the treasurer of the Northeastern Automotive Club.
      </p>
      <h2 className="text-2xl font-bold mb-4">Where I follow the market</h2>
      <ul className="list-disc pl-6 space-y-2">
        <li><a href="https://bringatrailer.com" className="hover:text-red-500">Bring a Trailer</a></li>
        <li><a href="https://carsandbids.com" className="hover:text-red-500">Cars & Bids</a></li>
        <li><a href="https://issimi.com" className="hover:text-red-500">ISSIMI</a></li>
      </ul>
    </main>
  );
}
