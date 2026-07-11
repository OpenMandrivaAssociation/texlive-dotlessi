%global tl_name dotlessi
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Provides dotless is and js for use in any math font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dotlessi
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dotlessi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dotlessi.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides two commands: \dotlessi and \dotlessj, which give
access to dotless i's and j's in math mode. They are intended for
symbols in non English languages.

