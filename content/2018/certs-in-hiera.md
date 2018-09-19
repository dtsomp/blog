Title: Distributing certificates with Hiera
Authors: dtsomp
Date: 2018-09-19

## Short intro

[Hiera](https://puppet.com/docs/puppet/5.3/hiera_intro.html) is what you should use to get data into Puppet's variables. [Hiera-eyaml](https://puppet.com/blog/encrypt-your-data-using-hiera-eyaml) is what you should use to make sure that data is encrypted when in rest (i.e. committed in a repository).

If you don't need to encrypt certificates (or other files) in a repository, then this article is not for you.

Why would you need to distribute certificates instead of creating them on the hosts themselves?
There are a couple of reasons. 
In my case it was a certificate provided by a third-party.
I am sure there are more use cases for this.

## Plain-text certificates

My biggest dislike about Hiera is the way that everything it handles is plain text. I mean, not dislike per se - everybody loves plain text, right? - but there is the issue of distributing files, like certificates.

PEM files are fine, they are already plain text. The way to handle them is to encrypt them:

```
$ eyaml encrypt -n gpg --gpg-recipients-file hiera-eyaml-gpg.recipients -f snakeoil.pem

string: ENC[GPG,hQEMAzQwoE+Gwj0aAQf+JbeDfSzWqt+xNP109+w+JENeIBn34D7s7...

OR
block: >
    ENC[GPG,hQEMAzQwoE+Gwj0aAQf+JbeDfSzWqt+xNP109+w+JENeIBn34D7s7wyYbaaS
    ocKN1/jk5TUTlmURnNz/Da7mMZfMiVGlGBni8MJQer7PTvWApVzo1lHtdQF/
    WTJvfp9pHOQ5XncYm7DXi8ZJnbQujFAXFzieUnEaavBZBFeNoXuCH92rbnLP
    f3oKQwEQetH4YEYvUxgmZl1Ww98rBL6m72LNZ+TG6iOM7dIgx2RWWT4Z0//G
    fNr2Sz3iU2243xtKA6hoRvlJzBOKPBvsoK8iDFd425Wo2gp54fG27fcQMT/I
	....
```

and then append one of the two forms to your eyaml file. The block format is usually sliiiiightly more readable.

```
cert::snakeoil_pem: >
ENC[GPG,hQEMAzQwoE+Gwj0aAQf+JbeDfSzWqt+xNP109+w+JENeIBn34D7s7wyYbaaS
    ocKN1/jk5TUTlmURnNz/Da7mMZfMiVGlGBni8MJQer7PTvWApVzo1lHtdQF/
    WTJvfp9pHOQ5XncYm7DXi8ZJnbQujFAXFzieUnEaavBZBFeNoXuCH92rbnLP
    f3oKQwEQetH4YEYvUxgmZl1Ww98rBL6m72LNZ+TG6iOM7dIgx2RWWT4Z0//G
    fNr2Sz3iU2243xtKA6hoRvlJzBOKPBvsoK8iDFd425Wo2gp54fG27fcQMT/I
	...
```

Then you can recreate the file on the Puppet host.

```
# puppet
file{'snakeoil.pem':
	content => lookup('cert::snakeoil_pem')
    ...
```

This is not an elegant solution. If you use `hiera-eyaml-gpg` (like we do), this text block is going to get huge.

## Binary certificates

If, however, you have to deal with a binary format (eg .p12), then there's an extra problem to deal with. `hiera-eyaml` et al seem to handle binary files pretty well. 
Hiera on the other hand seems to throw a hissy fit when it comes to reading variables containing binary.

When in doubt, `base64`.

```
$ base64 snakeoil.p12 | eyaml encrypt -n gpg --gpg-recipients hiera-eyaml-gpg.recipients --stdin

string: ENC[GPG,hQEMAzQwoE+Gwj0aAQf+JbeDfSzWqt+xNP109+w+JENeIBn34D7s7wy...

OR
block: >
    ENC[GPG,hQEMAzQwoE+Gwj0aAQf+JbeDfSzWqt+xNP109+w+JENeIBn34D7s7wyYbaaS
    ocKN1/jk5TUTlmURnNz/Da7mMZfMiVGlGBni8MJQer7PTvWApVzo1lHtdQF/
    WTJvfp9pHOQ5XncYm7DXi8ZJnbQujFAXFzieUnEaavBZBFeNoXuCH92rbnLP
    f3oKQwEQetH4YEYvUxgmZl1Ww98rBL6m72LNZ+TG6iOM7dIgx2RWWT4Z0//G
    fNr2Sz3iU2243xtKA6hoRvlJzBOKPBvsoK8iDFd425Wo2gp54fG27fcQMT/I
	....
```

Insert in your eyaml file as usual. When it's time to retrieve the certificate, don't forget to Base64-decode it.

```
file{'snakeoil_p12':
	content => base64('decode', lookup('cert::snakeoil_p12'))
    ...
```

That's not fun by any standard, but it works.

