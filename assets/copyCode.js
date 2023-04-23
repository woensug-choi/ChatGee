var codeBlocks = document.querySelectorAll('pre.highlight');

codeBlocks.forEach(function (codeBlock) {
  var copyButton = document.createElement('copybutton');
  copyButton.className = 'copy';
  copyButton.type = 'button';
  copyButton.ariaLabel = 'Copy code to clipboard';
  copyButton.innerText = 'Copy';

  codeBlock.append(copyButton);

  copyButton.addEventListener('click', function () {
    var code = codeBlock.querySelector('code').innerText.trim();
    window.navigator.clipboard.writeText(code);

    copyButton.innerText = 'Done';
    copyButton.style='background: rgb(0, 107, 70)'
    var fourSeconds = 4000;

    setTimeout(function () {
      copyButton.innerText = 'Copy';
      copyButton.style=''
    }, fourSeconds);
  });
});