Name:		texlive-dotlessi
Version:	51476
Release:	2
Summary:	Provides dotless i's and j's for use in any math font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dotlessi
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotlessi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dotlessi.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides two commands: \dotlessi and \dotlessj,
which give access to dotless i's and j's in math mode. They are
intended for symbols in non English languages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/dotlessi
%doc %{_texmfdistdir}/doc/latex/dotlessi

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
