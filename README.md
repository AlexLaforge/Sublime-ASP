# Sublime ASP

Enhancements for ASP handling in Sublime Text 3.


## Installation
On Windows, save `FixASP.sublime-package` to `%appdata%\Sublime Text 3\Installed Packages\`.

## Fixes

### Single quotes being doubled
Normally when you press the `'` key in ASP for a comment, it inserts two as though it were a string.

```ASP
<%
Dim test '' We don't need both of these quotes
%>
```

With this package, the default behavior is preserved except when creating a comment in ASP. In that case, a single quote and a space will be inserted instead.

### Improper syntax highlighting in script tags

Normally, an ASP comment in ASP tags in a script tag would break Sublime's syntax highlighting, causing it to think the rest of the file (until the next `'`) is a JavaScript string.
```ASP
<script>
<%
Dim test ' ASP comment in Javascript
%>
</script>
```

With this package, this behavior is fixed so that the comment and subsequent lines will be highlighted correctly.