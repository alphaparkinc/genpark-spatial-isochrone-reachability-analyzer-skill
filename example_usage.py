from client import SpatialIsochroneReachabilityAnalyzerClient

def main():
    client = SpatialIsochroneReachabilityAnalyzerClient()
    res = client.compute_isochrone_boundary(40.7128, -74.0060, 'CYCLING', 20)
    print('Isochrone Analyzer: ' + res['isochrone_id'] + ' (' + res['travel_mode'] + ' ' + str(res['cutoff_minutes']) + 'min)')
    print('Reach Radius: ' + str(res['estimated_reach_radius_km']) + 'km | Area: ' + str(res['accessible_area_sq_km']) + ' sq km')
    print('Polygon URL: ' + res['isochrone_polygon_url'])

if __name__ == '__main__':
    main()
