'use client'

import dynamic from 'next/dynamic'

const Map = dynamic(() => import('./Map'), {
  loading: () => <p>Loading Map...</p>,
  ssr: false
})

export default function MapWrapper() {
  return (
    <div className="flex-1">
      <Map />
    </div>
  )
}
