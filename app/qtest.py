import dramatiq

@dramatiq.actor
def test(x,y):
    return x * y
job = test.send(4, 4)
print(job)
print(job.get_results())