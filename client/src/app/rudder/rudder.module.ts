import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from '@angular/material';
import { SocketService } from '../shared';

import { RudderComponent } from './rudder.component';
import { RudderService } from './rudder.service';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    MaterialModule
  ],
  declarations: [RudderComponent],
  exports: [RudderComponent],
  providers: [RudderService, SocketService]
})
export class RudderModule { }
