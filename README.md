# blog-tutorial-just-spec

Hello, this is an example repository to demonstrate COPR SCM abilities.
Content of this repository is flat and packed. In addition, the sources
(<https://clime.fedorapeople.org/example-1.0.0.tar.gz>) are external and will be
downloaded by COPR during its build process.

**Flat** means there are no subpackages in the repository except the root one.
In other words, there are no subdirectories that would themselves contain a spec file.

**Packed** means the application source files are packed into a tarball
being referenced by a Source directive in the .spec file. Note that
the source tarball might not be actually present in the repository. Instead,
it can be provided externally through URL (specified in the "Source"
definition). The external sources will be then downloaded once needed
during the build process.

----

Note that for downloading to work, the repository content _needs_ to be **packed** 
(otherwise Source0 is created automatically). The easiest way to ensure that your 
repository is **packed** is to have at least one `Source` or `Patch` present in the
repository. If you don't have any of those, you need to stick to a limited set
of filenames that your repository might contain to be still recognized as **packed**
even though there is no `Source` or `Patch` present. This set include .spec file, hidden
files, `LICENSE`, `README`, `README.md`. See [blog-tutorial-flat-layered](
https://github.com/clime/blog-tutorial-layered) for the detailed discussion 
on the topic.
