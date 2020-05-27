function copyToClipboard(element){
    $(element).select();
    document.execCommand("copy");
}