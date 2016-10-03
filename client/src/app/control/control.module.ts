import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MaterialModule } from '@angular/material';
import { SocketService } from '../shared';

import { ControlComponent } from './control.component';
import { ControlService } from './control.service';

@NgModule({
  imports: [
    CommonModule,
    MaterialModule
  ],
  declarations: [ControlComponent],
  exports: [ControlComponent],
  providers: [ControlService, SocketService]
})
export class ControlModule { }
