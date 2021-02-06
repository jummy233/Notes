# easy description of the package dependecies
# based on generic autotools.

let
  pkgs = import <nixpkgs> {};
  mkDerivation = import ./autotools.nix pkgs; # partially apply
in
  mkDerivation {
    name = "hello";
    src = ./hello-2.10.tar.gz;
  }
