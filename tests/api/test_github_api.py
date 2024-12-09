import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user_defunkt = github_api.get_user("defunkt")
    assert user_defunkt["login"] == "defunkt"

@pytest.mark.api
def test_user_not_exists(github_api):
    user_butenkosergii = github_api.get_user("butenkosergii")
    assert user_butenkosergii["message"] == "Not Found"

@pytest.mark.api
def test_repo_can_be_found(github_api):
    result_of_search = github_api.search_repo("become-qa-auto")
    assert result_of_search["total_count"] == 58

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    result_of_search = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert result_of_search["total_count"] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    result_of_search_s = github_api.search_repo("s")
    assert result_of_search_s["total_count"] != 0

@pytest.mark.api
def test_list_releases_found(github_api):
    releases = github_api.list_releases("Natalinik", "NataliQA")
    assert len(releases) >= 1
    assert releases[0]["tag_name"] == "1.0.0"
    assert releases[0]["author"]["login"] == "Natalinik"

@pytest.mark.api
def test_list_releases_not_found(github_api):
    releases = github_api.list_releases("Natalinik", "QA")
    assert releases["status"] == "404"