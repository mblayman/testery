from testery import models


def _marshall_build(builds):
    marshalled_builds = []
    for build in builds:
        marshalled_builds.append({
            'id': build.id,
            'passes': build.passes,
            'fails': build.fails,
            'skips': build.skips,
        })
    marshalled = {'builds': marshalled_builds}
    return marshalled


MODEL_MAP = {
    models.Build: _marshall_build,
}


def marshall(model, content):
    """Marshall model instances to basic data types."""
    return MODEL_MAP[model](content)
