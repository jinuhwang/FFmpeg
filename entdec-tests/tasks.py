from invoke import task
import tempfile

DUMP = "./dump.sh"


@task
def make_install(ctx):
    ctx.run("make install -C .. -j`nproc`", echo=True)

@task
def check(ctx):
    INPUT = "/workspace/10m.mp4"
    GT_HASH = "9088fe510aea654fceea87a8113e470f"

    make_install(ctx)
    with tempfile.NamedTemporaryFile(mode='r') as f:
        ctx.run(f"{DUMP} {INPUT} {f.name}", echo=True)
        hashed = md5(ctx, f.name)

    print("*" * 30)
    print(hashed == GT_HASH)
    print("*" * 30)


@task
def md5(ctx, target):
    ret = ctx.run(f"md5sum {target}", echo=True)
    hashed = ret.stdout.split()[0]
    return hashed


@task
def visualize(ctx):
    make_install(ctx)
    INPUT = "/ssd3/h265/archie/day1-1s-crf-26-slow.mp4"
    OUTPUT = "/tmp/raw.dump"
    ctx.run(f"{DUMP} {INPUT} {OUTPUT}", echo=True)




