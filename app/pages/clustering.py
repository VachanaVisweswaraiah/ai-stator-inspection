from app.ui import render_page_title


def render(
    render_information,
    render_fitting_groups,
    render_clustering,
):
    render_page_title("Box and Cylinder Analysis")
    render_information()
    render_fitting_groups()
    render_clustering()
