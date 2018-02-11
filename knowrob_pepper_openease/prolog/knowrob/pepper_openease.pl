/*
  Copyright (C) 2018 Sascha Jongebloed
  All rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are met:
      * Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.
      * Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution.
      * Neither the name of the <organization> nor the
        names of its contributors may be used to endorse or promote products
        derived from this software without specific prior written permission.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

:- module(pepper_openease,
    [
      pepper_point_at/5,
      pepper_point_at/4,
      pepper_point_at/3,
      pepper_point_at/2,
      pepper_say/1
    ]).
/** <module> Interface for simple pepper point at functionality

@author Sascha Jongebloed
@license BSD
*/

:- use_foreign_library('libpepper_openease_client.so').
:- ros_init_pepper.

%% pepper_point_at(+X,+Y,+Z,+FrameID,+ToSay) is semidet.
%
% Calls the pepper_point_at service.

%% pepper_point_at(+X,+Y,+Z,+FrameID) is semidet.
%
% Calls the pepper_point_at service.
pepper_point_at(X,Y,Z,FrameID) :- pepper_point_at(X,Y,Z,FrameID,_).

%% pepper_point_at(+Translation,+FrameID) is semidet.
%
% Calls the pepper_point_at service.
pepper_point_at([X,Y,Z],FrameID) :- pepper_point_at(X,Y,Z,FrameID,_).


%% pepper_point_at(+Translation,+FrameID, +ToSay) is semidet.
%
% Calls the pepper_point_at service.
pepper_point_at([X,Y,Z],FrameID,ToSay) :- pepper_point_at(X,Y,Z,FrameID,ToSay).

%% pepper_say(+Message) is semidet.
%
% Calls the pepper_say service.


