class SpatialIsochroneReachabilityAnalyzerClient:
    def compute_isochrone_boundary(self, origin_lat=37.7833, origin_lng=-122.4167, travel_mode='WALKING', cutoff_minutes=15):
        approx_radius_km = round(cutoff_minutes * 0.08, 2)
        return {
            'isochrone_id': 'iso_ana_8812',
            'travel_mode': travel_mode,
            'cutoff_minutes': cutoff_minutes,
            'estimated_reach_radius_km': approx_radius_km,
            'accessible_area_sq_km': round(3.14159 * (approx_radius_km ** 2), 2),
            'pedestrian_transit_accessible': True,
            'isochrone_polygon_url': 'https://atlas.isochrone.genpark.ai/polygons/8812.json'
        }
