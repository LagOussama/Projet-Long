import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProtocolePlotComponent } from './protocole-plot.component';

describe('ProtocolePlotComponent', () => {
  let component: ProtocolePlotComponent;
  let fixture: ComponentFixture<ProtocolePlotComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProtocolePlotComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProtocolePlotComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
