import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from '@angular/material';
import { SocketService } from '../shared';

import { ThrottleComponent } from './throttle.component';
import { ThrottleService } from './throttle.service';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    MaterialModule
  ],
  declarations: [ThrottleComponent],
  exports: [ThrottleComponent],
  providers: [ThrottleService, SocketService]
})
export class ThrottleModule { }
