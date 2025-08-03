let
  pkgs = import <nixpkgs> { };
in
pkgs.mkShell {
  packages = with pkgs; [
    python314
    python313Packages.pillow
    python313Packages.tqdm
  ];
}
