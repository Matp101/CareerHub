#flask shell

from sql.data import job_listings_data, categories

from website import create_app, db
from website.models import JobListing, JobCategory
from datetime import datetime

app = create_app()
app.app_context().push()


for i in categories:
    category = JobCategory(category_id=int(i[0]), category_name=i[1])
    db.session.add(category)

l = job_listings_data
for listing_data in l:
    date_posted = datetime.strptime(listing_data[9], "%Y-%m-%d %H:%M:%S")
    job_category = db.session.query(JobCategory).filter_by(category_id=int(listing_data[8])).first()
    job_listing = JobListing(
        job_id=listing_data[0],
        title=listing_data[1],
        company=listing_data[2],
        salary=int(listing_data[3]),
        location=listing_data[4],
        type=listing_data[5],
        description=listing_data[6],
        email=listing_data[7],
        date_posted=date_posted,
        category_id=job_category.category_id 
    )
    db.session.add(job_listing)


db.session.commit()