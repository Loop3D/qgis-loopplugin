import rasterio
from pyproj import Transformer

# Path to your DTM file


def extract_bbox(self, dtm_file):
    # Open the DTM file
    with rasterio.open(dtm_file) as src:
        print(f"dtm file is {dtm_file}")
        # Get the current CRS of the DTM file
        dtm_crs = src.crs
        # print(f"DTM CRS: {dtm_crs}")

        # Get the bounding box in the current CRS
        minx, miny, maxx, maxy = src.bounds
        # print(f"Bounding Box in original CRS: {minx}, {miny}, {maxx}, {maxy}")
        # try:
        # If the DTM is already in UTM, you're done! Just use minx, miny, maxx, maxy
        # if dtm_crs.is_projected:
        # print(
        #     f"Bounding Box in UTM (original CRS): {minx}, {miny}, {maxx}, {maxy}"
        # )

        try:
            return minx, miny, maxx, maxy
        except:
            # else:
            # If the DTM is in a geographic CRS (e.g., WGS84), convert it to UTM
            # Define a transformer to UTM (replace "EPSG:32633" with your desired UTM zone)
            transformer = Transformer.from_crs(dtm_crs, "EPSG:32633", always_xy=True)

            # Convert the bounding box coordinates to UTM
            minx_utm, miny_utm = transformer.transform(minx, miny)
            maxx_utm, maxy_utm = transformer.transform(maxx, maxy)

            # print(
            #     f"Bounding Box in UTM: {minx_utm}, {miny_utm}, {maxx_utm}, {maxy_utm}"
            # )
            return minx_utm, miny_utm, maxx_utm, maxy_utm
        # except:
        #     return minx, miny, maxx, maxy

    return
