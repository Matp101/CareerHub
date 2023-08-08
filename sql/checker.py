from jobs import jobs


if __name__ == "__main__":
    title_to_ids = {}
    all_ids = []
    duplicate_ids = set()

    for job in jobs:
        job_id, job_title = job[0], job[1]
        all_ids.append(job_id)  # Store all IDs in order
        if job_title in title_to_ids:
            title_to_ids[job_title].append(job_id)
            duplicate_ids.add(job_id)  # Add ID to duplicates set
        else:
            title_to_ids[job_title] = [job_id]

    for title, ids in title_to_ids.items():
        if len(ids) > 1:
            print(f"Duplicate job title '{title}' found with IDs: {', '.join(ids)}")

    print("Total number of matching IDs:", len(duplicate_ids))
    print("All job IDs in order:", ', '.join(all_ids))