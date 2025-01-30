import MapWrapper from '../components/MapWrapper'

export default function Home() {
  return (
    <div className="flex flex-col h-screen">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="mx-auto max-w-7xl px-4 py-4 sm:px-6 lg:px-8">
          <h1 className="text-2xl font-bold tracking-tight text-gray-900">GIS Web Platform</h1>
        </div>
      </header>

      {/* Main Content */}
      <div className="flex-1 flex">
        {/* Sidebar */}
        <div className="w-64 bg-white shadow-lg">
          <div className="h-full px-3 py-4 overflow-y-auto">
            <div className="space-y-2">
              <button className="w-full flex items-center p-2 text-gray-900 rounded-lg hover:bg-gray-100">
                <span className="ml-3">Layer Controls</span>
              </button>
              <button className="w-full flex items-center p-2 text-gray-900 rounded-lg hover:bg-gray-100">
                <span className="ml-3">Analysis Tools</span>
              </button>
              <button className="w-full flex items-center p-2 text-gray-900 rounded-lg hover:bg-gray-100">
                <span className="ml-3">Export Data</span>
              </button>
            </div>
          </div>
        </div>

        {/* Map Container */}
        <MapWrapper />
      </div>
    </div>
  )
}
