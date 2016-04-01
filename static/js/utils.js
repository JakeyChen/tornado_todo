/**
 * 获取_xsrf cookie getCookie("_xsrf")
 */
function getCookie(name) {
    var c = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return c ? c[1] : undefined;
}

/**
 * empty check
 */
function emptyCheck(id) {
    var txt = document.getElementById(id).value
    if (txt.length == 0) {
        alert("Input can't be empty.")
        return false;
    }
    return true;
}
